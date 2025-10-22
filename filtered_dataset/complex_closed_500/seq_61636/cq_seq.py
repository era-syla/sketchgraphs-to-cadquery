import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.00215, 0.01542).lineTo(0.00215, 0.01542).lineTo(0.00215, 0.01292).lineTo(-0.00215, 0.01292).lineTo(-0.00215, 0.01542).close()
solid=wp_sketch0.add(loop0).extrude(-0.0008286236670031543)
