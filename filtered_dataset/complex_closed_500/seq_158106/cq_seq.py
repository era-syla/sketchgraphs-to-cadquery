import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.108, -0.1015).lineTo(-0.108, -0.1015).lineTo(-0.108, 0.1015).lineTo(0.108, 0.1015).lineTo(0.108, -0.1015).close()
solid=wp_sketch0.add(loop0).extrude(0.1816387539206738)
