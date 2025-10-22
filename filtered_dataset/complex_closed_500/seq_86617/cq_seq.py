import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.20003, 0.14287).lineTo(0.33338, 0.14287).lineTo(0.33338, 0.0).lineTo(-0.20003, 0.0).lineTo(-0.20003, 0.14287).close()
solid=wp_sketch0.add(loop0).extrude(-1.2500771056591589)
