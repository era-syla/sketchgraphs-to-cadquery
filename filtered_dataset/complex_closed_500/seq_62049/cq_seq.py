import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.04876, -0.10734).lineTo(-0.03987, -0.10734).lineTo(-0.03987, -0.09553).lineTo(-0.04876, -0.09553).lineTo(-0.04876, -0.10734).close()
solid=wp_sketch0.add(loop0).extrude(0.029244850474832138)
