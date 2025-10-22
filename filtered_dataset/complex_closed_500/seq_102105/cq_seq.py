import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.01522, 0.00397).lineTo(-0.03558, 0.00397).lineTo(-0.03558, 0.00905).lineTo(0.01522, 0.00905).lineTo(0.01522, 0.00397).close()
solid=wp_sketch0.add(loop0).extrude(0.05137789703325518)
