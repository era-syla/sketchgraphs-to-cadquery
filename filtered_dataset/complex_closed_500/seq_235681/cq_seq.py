import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.125, -0.00775).lineTo(0.125, -0.00775).lineTo(0.125, -0.00175).lineTo(-0.125, -0.00175).lineTo(-0.125, -0.00775).close()
solid=wp_sketch0.add(loop0).extrude(-0.4140248319711617)
