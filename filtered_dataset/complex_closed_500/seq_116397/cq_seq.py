import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, -0.01542).lineTo(0.0, 0.01542).lineTo(0.029, 0.01542).lineTo(0.029, 0.01142).lineTo(0.004, 0.01142).lineTo(0.004, -0.01042).lineTo(0.028, -0.01042).lineTo(0.028, -0.00825).lineTo(0.035, -0.00825).lineTo(0.035, -0.01542).lineTo(0.0, -0.01542).close()
solid=wp_sketch0.add(loop0).extrude(0.010446376276986547)
