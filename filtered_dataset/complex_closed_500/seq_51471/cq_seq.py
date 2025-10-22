import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0615, -0.09).lineTo(-0.0615, -0.09).lineTo(-0.0615, 0.09).lineTo(0.0615, 0.09).lineTo(0.0615, -0.09).close()
solid=wp_sketch0.add(loop0).extrude(0.19607747939167153)
