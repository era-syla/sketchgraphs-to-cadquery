import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.01485, 0.01245).lineTo(0.05715, 0.01245).lineTo(0.05715, -0.00355).lineTo(-0.01485, -0.00355).lineTo(-0.01485, 0.01245).close()
solid=wp_sketch0.add(loop0).extrude(-0.10112285278125183)
