import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.00403, -0.02).lineTo(-0.00403, -0.01).lineTo(0.00403, -0.01).lineTo(0.00403, -0.02).lineTo(-0.00403, -0.02).close()
solid=wp_sketch0.add(loop0).extrude(0.01505189850326537)
