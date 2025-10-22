import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(-0.02837, 0.0).lineTo(-0.04177, 0.04714).lineTo(-0.03467, 0.04714).lineTo(-0.03882, 0.05635).lineTo(0.0, 0.05635).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.07348045700486144)
