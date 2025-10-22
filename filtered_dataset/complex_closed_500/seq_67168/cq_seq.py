import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.00861, -0.00342).lineTo(0.00413, -0.00342).lineTo(0.00413, 0.0179).lineTo(-0.00861, 0.0179).lineTo(-0.00861, -0.00342).close()
solid=wp_sketch0.add(loop0).extrude(0.018078818932965167)
