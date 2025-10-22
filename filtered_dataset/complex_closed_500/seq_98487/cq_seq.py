import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.24514, -0.05566).lineTo(0.11659, -0.05566).lineTo(0.11659, 0.00848).lineTo(0.27507, 0.00811).lineTo(0.27507, -0.05566).lineTo(0.24514, -0.05566).close()
solid=wp_sketch0.add(loop0).extrude(-0.15332244618539168)
