import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.01248, -0.00375).lineTo(-0.01998, -0.00375).lineTo(-0.01998, 0.00375).lineTo(-0.01248, 0.00375).lineTo(-0.01248, -0.00375).close()
solid=wp_sketch0.add(loop0).extrude(-0.01576125826084042)
