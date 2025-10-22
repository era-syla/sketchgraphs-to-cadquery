import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.00323, -0.03175).lineTo(-0.00312, -0.03175).lineTo(-0.00312, -0.01143).lineTo(0.00323, -0.01143).lineTo(0.00323, -0.03175).close()
solid=wp_sketch0.add(loop0).extrude(-0.006289399453975841)
