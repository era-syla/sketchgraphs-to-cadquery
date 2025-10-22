import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.10852, 0.07503).lineTo(0.11348, 0.07503).lineTo(0.11348, -0.07697).lineTo(-0.10852, -0.07697).lineTo(-0.10852, 0.07503).close()
solid=wp_sketch0.add(loop0).extrude(0.21465888218539236)
