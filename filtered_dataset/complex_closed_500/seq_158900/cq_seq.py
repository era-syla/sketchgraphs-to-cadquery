import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(2.08193, 1.05883).lineTo(1.68823, 1.05883).lineTo(1.68823, 2.25263).lineTo(2.08193, 2.25263).lineTo(2.08193, 1.05883).close()
solid=wp_sketch0.add(loop0).extrude(2.1585394090271413)
