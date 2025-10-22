import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.01753, 0.05014).lineTo(-0.02057, 0.05014).lineTo(-0.02057, 0.02474).lineTo(-0.04597, 0.02474).lineTo(-0.04597, -0.01336).lineTo(0.04293, -0.01336).lineTo(0.04293, 0.02474).lineTo(0.01753, 0.05014).close()
solid=wp_sketch0.add(loop0).extrude(-0.17376737085574878)
