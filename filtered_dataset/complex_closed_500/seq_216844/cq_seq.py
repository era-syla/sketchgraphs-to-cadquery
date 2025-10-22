import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.04826, 0.02286).lineTo(0.00254, 0.02286).lineTo(0.00254, 0.00254).lineTo(0.04826, 0.00254).lineTo(0.04826, 0.02286).close()
solid=wp_sketch0.add(loop0).extrude(0.11398881931220414)
