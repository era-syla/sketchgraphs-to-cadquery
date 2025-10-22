import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0, -0.0).lineTo(0.07936, -0.0).lineTo(0.07936, -0.127).lineTo(-0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.08837978624809871)
