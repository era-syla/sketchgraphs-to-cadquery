import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.127, 0.0).lineTo(0.0, 0.0).lineTo(0.0, 0.0254).lineTo(0.0254, 0.0254).lineTo(0.0254, 0.01458).lineTo(0.0762, 0.01458).lineTo(0.0762, 0.0254).lineTo(0.127, 0.0254).lineTo(0.127, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.33675228699245857)
