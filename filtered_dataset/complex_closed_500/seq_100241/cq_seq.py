import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.01717, -0.07562).lineTo(0.01741, -0.07562).lineTo(0.01741, -0.14429).lineTo(-0.01717, -0.14429).lineTo(-0.01717, -0.07562).close()
solid=wp_sketch0.add(loop0).extrude(0.14435667683894599)
