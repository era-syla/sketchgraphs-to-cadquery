import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.012, 0.0).lineTo(-0.0, 0.0).lineTo(0.0, 0.0162).lineTo(-0.012, 0.0162).lineTo(-0.012, 0.0262).lineTo(0.00345, 0.02206).lineTo(0.06, -0.01059).lineTo(0.06, -0.03192).lineTo(0.02277, -0.00068).lineTo(-0.012, -0.01).lineTo(-0.012, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.012311711270039502)
