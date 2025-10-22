import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0055, 0.0016).lineTo(0.004, 0.0016).lineTo(0.004, 0.00435).lineTo(0.0055, 0.00522).lineTo(0.0055, 0.0016).close()
solid=wp_sketch0.add(loop0).extrude(0.006743971353229723)
