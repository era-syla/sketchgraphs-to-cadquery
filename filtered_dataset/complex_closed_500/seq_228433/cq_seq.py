import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.097, 0.2075).lineTo(-0.097, 0.1675).lineTo(-0.044, 0.1675).lineTo(-0.044, 0.2075).lineTo(-0.097, 0.2075).close()
solid=wp_sketch0.add(loop0).extrude(-0.154882524185886)
