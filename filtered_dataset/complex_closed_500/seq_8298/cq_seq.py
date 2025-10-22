import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.03544).lineTo(0.0, 0.0).lineTo(0.15874, 0.0).lineTo(0.15874, 0.03445).lineTo(-0.0, 0.03544).close()
solid=wp_sketch0.add(loop0).extrude(-0.38835983529104406)
