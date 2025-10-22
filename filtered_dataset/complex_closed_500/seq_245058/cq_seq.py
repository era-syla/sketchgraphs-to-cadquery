import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 2.6).lineTo(0.0, 2.4).lineTo(5.0, 3.2).lineTo(4.9688, 3.39501).lineTo(-0.0, 2.6).close()
solid=wp_sketch0.add(loop0).extrude(-7.900510042338463)
