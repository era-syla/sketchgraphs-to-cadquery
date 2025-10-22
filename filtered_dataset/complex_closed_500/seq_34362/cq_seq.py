import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.00068, 0.00116).lineTo(0.00087, 0.00116).lineTo(0.00087, 0.00351).lineTo(-0.00068, 0.00351).lineTo(-0.00068, 0.00116).close()
solid=wp_sketch0.add(loop0).extrude(0.0034827068566790067)
