import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.02159, 0.00577).lineTo(0.02009, 0.00577).lineTo(0.02009, 0.0077).lineTo(0.02159, 0.0077).lineTo(0.02159, 0.00577).close()
solid=wp_sketch0.add(loop0).extrude(0.005423692099882178)
