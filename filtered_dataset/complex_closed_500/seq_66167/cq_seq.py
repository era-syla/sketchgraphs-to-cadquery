import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0254, -0.0508).lineTo(0.0762, -0.0508).lineTo(0.0254, -0.0254).lineTo(0.0254, -0.0508).close()
solid=wp_sketch0.add(loop0).extrude(0.12001168663350081)
