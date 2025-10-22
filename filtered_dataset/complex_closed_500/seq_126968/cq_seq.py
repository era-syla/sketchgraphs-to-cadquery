import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.065, -0.05).lineTo(-0.065, -0.05).lineTo(-0.065, -0.08).lineTo(0.065, -0.08).lineTo(0.065, -0.05).close()
solid=wp_sketch0.add(loop0).extrude(0.021169376112780074)
