import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.02741, 0.01814).lineTo(-0.04312, 0.00907).lineTo(-0.04312, -0.00907).lineTo(-0.02941, -0.01698).lineTo(-0.02941, -0.03281).lineTo(-0.01371, -0.04188).lineTo(-0.0, -0.03396).lineTo(0.01371, -0.04188).lineTo(0.02941, -0.03281).lineTo(0.02941, -0.01698).lineTo(0.04312, -0.00907).lineTo(0.04312, 0.00907).lineTo(0.02741, 0.01814).lineTo(0.01371, 0.01022).lineTo(0.0, 0.01814).lineTo(-0.01371, 0.01022).lineTo(-0.02741, 0.01814).close()
solid=wp_sketch0.add(loop0).extrude(0.014486021083110593)
