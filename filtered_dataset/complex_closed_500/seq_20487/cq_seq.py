import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-3.77628, -3.065).lineTo(-5.31244, -4.35398).lineTo(-7.29284, -8.60098).lineTo(-7.25206, -8.62).lineTo(-5.27587, -4.38204).lineTo(-3.70628, -3.065).lineTo(-3.77628, -3.065).close()
solid=wp_sketch0.add(loop0).extrude(14.340231433010002)
