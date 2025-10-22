import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.04066, 0.00731).lineTo(0.10934, 0.00731).lineTo(0.10934, -0.06889).lineTo(-0.04066, -0.06889).lineTo(-0.04066, 0.00731).close()
solid=wp_sketch0.add(loop0).extrude(0.2430084225770039)
