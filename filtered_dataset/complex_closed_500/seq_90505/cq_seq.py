import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.054, 0.0).lineTo(-0.054, 0.0).lineTo(-0.054, -0.1).lineTo(0.054, -0.1).lineTo(0.054, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.16422580167094486)
