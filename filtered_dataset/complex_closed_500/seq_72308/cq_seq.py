import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.14, 0.0).lineTo(0.405, 0.0).lineTo(0.405, 0.20361).lineTo(0.37, 0.20361).lineTo(0.37, 0.23).lineTo(0.405, 0.23).lineTo(0.405, 0.20361).lineTo(0.14, -0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.7471730832508657)
