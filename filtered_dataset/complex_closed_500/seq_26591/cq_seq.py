import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.008, 0.03507).lineTo(0.002, 0.03507).lineTo(0.002, 0.02307).lineTo(0.008, 0.02307).lineTo(0.008, 0.03507).close()
solid=wp_sketch0.add(loop0).extrude(-0.031956313526805495)
