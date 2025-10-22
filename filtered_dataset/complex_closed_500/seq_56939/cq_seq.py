import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.00173, 0.01152).lineTo(0.07127, 0.01152).lineTo(0.07127, 0.005).lineTo(0.0252, 0.005).lineTo(0.00173, 0.01152).close()
solid=wp_sketch0.add(loop0).extrude(-0.12883765710791267)
