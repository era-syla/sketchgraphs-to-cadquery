import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-2.62669, 17.57867).lineTo(1.87331, 17.57867).lineTo(1.87331, -9.42133).lineTo(-2.62669, -9.42133).lineTo(-2.62669, 17.57867).close()
solid=wp_sketch0.add(loop0).extrude(-73.55493841258101)
