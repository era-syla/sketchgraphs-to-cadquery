import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.09934, 0.01616).lineTo(0.11433, 0.01616).lineTo(0.11433, 0.03656).lineTo(0.09934, 0.03656).lineTo(0.09934, 0.01616).close()
solid=wp_sketch0.add(loop0).extrude(0.0399276706903457)
