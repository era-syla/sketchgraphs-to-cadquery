import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.04888, 0.03962).lineTo(-0.00798, 0.03962).lineTo(-0.00798, -0.07152).lineTo(-0.04888, -0.07152).lineTo(-0.04888, 0.03962).close()
solid=wp_sketch0.add(loop0).extrude(-0.13108904565956167)
