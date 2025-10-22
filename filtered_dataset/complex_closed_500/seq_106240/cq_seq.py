import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.01945, 0.08894).lineTo(0.05727, 0.08894).lineTo(0.05727, 0.03499).lineTo(0.01945, 0.03499).lineTo(0.01945, 0.08894).close()
solid=wp_sketch0.add(loop0).extrude(-0.08201932470989223)
