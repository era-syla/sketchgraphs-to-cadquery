import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-5.66658, -8.34085).lineTo(-3.99735, -4.27275).lineTo(-2.32813, -8.34085).lineTo(-5.66658, -8.34085).close()
solid=wp_sketch0.add(loop0).extrude(10.926611273466651)
