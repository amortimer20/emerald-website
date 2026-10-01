// Marks a code block that holds box-drawing characters, such as the tables and panels that
// `Console.table` and `Console.panel` print, with the class `box-art`. src/styles/reference.css
// gives those blocks the line height at which JetBrains Mono's vertical lines join up.
const BOX_DRAWING = /[─-╿]/;

export function pluginBoxArt() {
	return {
		name: 'box-art',
		hooks: {
			postprocessRenderedBlock: ({ codeBlock, renderData }) => {
				if (!BOX_DRAWING.test(codeBlock.code)) return;
				const properties = (renderData.blockAst.properties ??= {});
				const classes = Array.isArray(properties.className) ? properties.className : [];
				properties.className = [...classes, 'box-art'];
			},
		},
	};
}
