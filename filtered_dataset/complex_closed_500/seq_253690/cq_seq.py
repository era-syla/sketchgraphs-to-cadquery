import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.07685, -0.004).lineTo(0.09685, -0.004).lineTo(0.09685, -0.024).lineTo(0.07685, -0.024).lineTo(0.07685, -0.004).close()
solid=wp_sketch0.add(loop0).extrude(0.04812627734037561)
