import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.1397, -0.8728).lineTo(0.1397, -0.8728).lineTo(0.1397, -0.67945).lineTo(-0.1397, -0.67945).lineTo(-0.1397, -0.8728).close()
solid=wp_sketch0.add(loop0).extrude(0.5004830238843884)
