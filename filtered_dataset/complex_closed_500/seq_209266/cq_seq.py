import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.05364, -0.01651).lineTo(0.06656, -0.01651).lineTo(0.06656, -0.03429).lineTo(0.05364, -0.03429).lineTo(0.05364, -0.01651).close()
solid=wp_sketch0.add(loop0).extrude(-0.014611848803202626)
