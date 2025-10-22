import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.03807, -0.04861).lineTo(-0.03807, -0.04861).lineTo(-0.03807, 0.04861).lineTo(0.03807, 0.04861).lineTo(0.03807, -0.04861).close()
solid=wp_sketch0.add(loop0).extrude(0.027862328318452752)
