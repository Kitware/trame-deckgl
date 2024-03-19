import { createDeck } from '@deck.gl/jupyter-widget';

export default {
  name: 'TrameDeck',
  props: {
    mapboxApiKey: {
      type: String,
    },
    jsonInput: {
      type: Object,
    },
    tooltip: {
      type: Boolean,
      default: false,
    },
    customLibraries: {
      type: Object,
    },
  },
  watch: {
    async jsonInput() {
      await this.mountVis();
    },
    async opt() {
      await this.mountVis();
    },
  },
  methods: {
    async mountVis() {
      this.unmoutViz();
      if (this.jsonInput && this.$el) {
        const { $el: container, jsonInput, tooltip, customLibraries, mapboxApiKey } = this;

        this.viz = createDeck({
          container,
          jsonInput,
          tooltip,
          customLibraries,
          mapboxApiKey,
        });
      }
    },
    unmoutViz() {
      if (this.viz) {
        this.viz.finalize();
        this.viz = null;
      }
    },
  },
  async mounted() {
    await this.mountVis();
  },
  beforeDestroy() {
    this.unmoutViz();
  },
  template: `<div></div>`,
};
