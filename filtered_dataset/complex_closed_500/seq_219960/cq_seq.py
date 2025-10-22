import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.47308, 0.1016).lineTo(0.44133, 0.1016).lineTo(0.44133, -0.0).lineTo(-0.47308, 0.0).lineTo(-0.47308, 0.1016).close()
solid=wp_sketch0.add(loop0).extrude(1.191173844907252)
