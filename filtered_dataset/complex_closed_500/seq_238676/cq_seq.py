import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.47347, -0.24012).lineTo(0.56237, -0.24012).lineTo(0.56237, -0.27822).lineTo(0.47347, -0.27822).lineTo(0.47347, -0.24012).close()
solid=wp_sketch0.add(loop0).extrude(0.24019208478751397)
