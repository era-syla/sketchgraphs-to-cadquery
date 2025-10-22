import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.0762, 0.0).lineTo(0.0762, 0.0254).lineTo(0.00975, 0.0254).lineTo(-0.0, -0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.019395731082561433)
