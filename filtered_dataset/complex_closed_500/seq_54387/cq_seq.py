import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.005, 0.01222).lineTo(0.005, 0.01222).lineTo(0.005, -0.01222).lineTo(-0.005, -0.01222).lineTo(-0.005, 0.01222).close()
solid=wp_sketch0.add(loop0).extrude(-0.052819546114881696)
